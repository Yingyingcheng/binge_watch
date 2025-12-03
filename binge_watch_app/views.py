from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Content, Review
from .forms import ReviewForm
from django.urls import reverse # Required for clean redirect

# -------------------------------------------------------------
# --- MAIN DASHBOARD VIEW (content_list) ---
# -------------------------------------------------------------

@login_required 
def content_list(request):
    # 1. Fetch ALL Content
    contents = Content.objects.all().order_by('title')
    review_form = ReviewForm()

    # --- HANDLE FORM SUBMISSION (POST) ---
    if request.method == 'POST':
        content_id = request.POST.get('content_id')
        
        if content_id:
            target_content = get_object_or_404(Content, pk=content_id)
            
            # 1. Check for existing review (Crucial for Update-or-Create logic)
            existing_review = Review.objects.filter(
                user=request.user, 
                content=target_content
            ).first()

            # Pass the existing instance to the form if found (forces UPDATE)
            submitted_form = ReviewForm(request.POST, instance=existing_review) 
            
            if submitted_form.is_valid():
                new_review = submitted_form.save(commit=False)
            
                
                if not existing_review:
                    new_review.user = request.user 
                    new_review.content = target_content 
            
                new_review.save()
                
                # Redirect using reverse() for a clean, non-cached GET request
                return redirect(reverse('content_list'))
            else:
                print("\n====================================")
                print("🚨 FORM SUBMISSION FAILED 🚨")
                print("User:", request.user)
                # This is the line that will give you the answer:
                print("Errors:", submitted_form.errors) 
                print("====================================\n")
                review_form = submitted_form 

    
    # --- PREPARE DATA FOR TEMPLATE (GET) ---

    overall_averages = Review.objects.aggregate(
        overall_avg_quality=Avg('quality_score'),
        overall_avg_risk=Avg('binge_risk_score')
    )
    user_history = Review.objects.filter(
        user=request.user
    ).select_related('content').order_by('-id') 

    context = {
        'contents': contents, 
        'review_form': review_form,
        'user_history': user_history,
    
        'overall_avg_quality': overall_averages.get('overall_avg_quality'),
        'overall_avg_risk': overall_averages.get('overall_avg_risk'),
    }
    return render(request, 'binge_watch/content_list.html', context)

# -------------------------------------------------------------
# --- OPTIONAL: Separate Review Page View (add_review) ---
# -------------------------------------------------------------

@login_required 
def add_review(request, content_id):
    """Allows a logged-in user to submit a review for specific content."""
    content = get_object_or_404(Content, pk=content_id)
    # Check if the user has already reviewed this content
    existing_review = Review.objects.filter(user=request.user, content=content).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=existing_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.content = content
            review.save()
            return redirect(reverse('content_list'))
    else:
        # Pre-populate form if an existing review is found (for editing)
        form = ReviewForm(instance=existing_review)

    context = {
        'content': content,
        'form': form
    }
    return render(request, 'binge_watch/add_review.html', context)