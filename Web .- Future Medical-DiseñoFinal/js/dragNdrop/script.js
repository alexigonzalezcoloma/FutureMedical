var dnd = dragNdrop({
  // element to be dragged (single DOM element)
  element: document.getElementById('element1'),
  // dropElements and/or CSS Selector(s) (false / DOM element(s))
  dropZones: [
    document.getElementById('dropZone1'),
    document.getElementById('dropZone2')
  ],
});