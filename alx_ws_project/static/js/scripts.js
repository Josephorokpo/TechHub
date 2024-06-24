document.addEventListener('DOMContentLoaded', function() {
  const commentToggle = document.getElementById('commentToggle');
  if (commentToggle) {
    commentToggle.addEventListener('click', function() {
      const commentForm = document.getElementById('commentForm');
      if (commentForm.style.display === 'none' || !commentForm.style.display) {
        commentForm.style.display = 'block';
      } else {
        commentForm.style.display = 'none';
      }
    });
  }

  const replyLinks = document.querySelectorAll('.reply-link');
  replyLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const commentId = this.dataset.commentId;
      const replyForm = document.querySelector(`.reply-form[data-parent-id="${commentId}"]`);
      replyForm.style.display = replyForm.style.display === 'none' || !replyForm.style.display ? 'block' : 'none';
    });
  });
});
