# Banner Gallery

<style>
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 14px;
  margin: 12px 0 24px 0;
}
.gallery-card {
  display: block;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 6px rgba(0,0,0,.08);
  text-decoration: none;
  background: var(--md-default-bg-color, #fff);
  border: 1px solid rgba(0,0,0,.06);
  transition: transform .08s ease, box-shadow .2s ease;
}
.gallery-card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.12); }
.gallery-card img {
  width: 100%; height: 140px; object-fit: cover; display: block; background: #eee;
}
.gallery-card .content { padding: 10px 12px; }
.gallery-card h3 { margin: 0 0 6px 0; font-size: 1rem; line-height: 1.2; }
.gallery-meta { color: #666; font-size: .85rem; }
.gallery-empty {
  border-radius: 12px; padding: 14px 16px; border: 1px dashed rgba(0,0,0,.2);
  background: rgba(0,0,0,.02);
}
</style>

<p class="gallery-meta">Browse all banners created from the CSV.</p>

<div class="gallery-grid" id="gallery-root">
<!-- GALLERY -->
</div>

<div class="gallery-empty" id="gallery-empty">
  No banners found yet. Once the build step writes cards into the
  <code>&lt;!-- GALLERY --&gt;</code> slot above, they will appear here.
</div>

<script>
(function(){
  var root = document.getElementById('gallery-root');
  var empty = document.getElementById('gallery-empty');
  if (root && empty && root.querySelector('.gallery-card')) {
    empty.style.display = 'none';
  }
})();
</script>
