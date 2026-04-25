from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """ A home page for Blog."""
    latest_posts = Post.objects.all()[:5]  # Last 5 posts
    context = {'latest_posts': latest_posts}
    return render(request, 'blogs/index.html', context)

def posts(request):
    """ Show all posts."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """ Show a single post."""
    post = get_object_or_404(Post,id=post_id)
    comments = post.comments.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """Adds a new post."""
    if request.method != 'POST':
        # No  data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blogs:posts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edits an existing post."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect('blogs:post', post_id=post.id)

    if request.method != 'POST':
        # Initial request; pre-fill form with current post.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    """Allows a logged-in user delete a post."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You do not have permission to delete this post.")
        return redirect('blogs:post', post_id=post.id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('blogs:posts')

    return render(request, 'blogs/delete_post.html', {'post': post})

@login_required
def add_comment(request, post_id):
    """Add a comment to a post using CommentForm."""

    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            return redirect('blogs:post', post_id=post.id)

    else:
        form = CommentForm()

    return render(request, 'blogs/add_comment.html', {
        'post': post,
        'form': form
    })

@login_required
def delete_comment(request, comment_id):
    """Delete a comment (only owner can delete)."""

    comment = get_object_or_404(Comment, id=comment_id, post=post)

    # permission check
    if comment.user != request.user:
        return redirect('blogs:post', post_id=comment.post.id)

    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        return redirect('blogs:post', post_id=post_id)

    return render(request, 'blogs/delete_comment.html', {
        'comment': comment
    })