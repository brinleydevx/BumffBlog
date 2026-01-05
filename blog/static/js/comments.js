// Toggle hidden reply groups
document.addEventListener('DOMContentLoaded', function(){
  document.querySelectorAll('.show-more-replies').forEach(function(btn){
    btn.addEventListener('click', function(e){
      var id = this.getAttribute('data-target');
      var el = document.getElementById(id);
      if(!el) return;
      if(el.style.display === 'none' || el.style.display === ''){
        el.style.display = 'block';
        this.textContent = 'Hide replies';
      } else {
        el.style.display = 'none';
        // extract count from data-target label (best-effort)
        var hidden = el.querySelectorAll('.comment').length;
        this.textContent = 'Show ' + hidden + ' more replies';
      }
    });
  });
});
