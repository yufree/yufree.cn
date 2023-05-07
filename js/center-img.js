(function() {
  function center_el(tagName) {
    var tags = document.getElementsByTagName(tagName), i, tag;
    for (i = 0; i < tags.length; i++) {
      tag = tags[i];
      var parent = tag.parentElement;
      // center an image if it is the only element of its parent
      if (parent.childElementCount === 1) {
        // if there is a link on image, check grandparent
        if (parent.nodeName === 'A') {
          parent = parent.parentElement;
          if (parent.childElementCount > 1) continue;
        }
        if (parent.nodeName === 'P') parent.style.textAlign = 'center';
      }
    }
  }
  var tagNames = ['img', 'embed', 'object'];
  for (var i = 0; i < tagNames.length; i++) {
    center_el(tagNames[i]);
  }
})();
