const $ = require('../static/jquery-3.4.1.min')
const initialize = require('../static/list.js')

// fix for testing :hidden/:visible jQuery selectors in jsDom
// source: https://github.com/jsdom/jsdom/issues/1048#issuecomment-401599392
window.Element.prototype.getClientRects = function() {
    var node = this;
    while(node) {
        if(node === document) {
            break;
        }
        // don't know why but style is sometimes undefined
        if (!node.style || node.style.display === 'none' || node.style.visibility === 'hidden') {
            return [];
        }
        node = node.parentNode;
    }
     var self = $(this);
    return [{width: self.width(), height: self.height()}];
};

describe('test visibility of .has-error CSS classes on text inputs', () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <form>
        <input name="text" />
        <div class="has-error">Error text</div>
      </form>
    `

    initialize()
  })

  test("errors should be hidden on keypress", () => {
    $('input[name="text"]').trigger('keypress')
    expect($('.has-error').is(':visible')).toBeFalsy()
  })

  test("errors aren't hidden if there is no keypress", () => {
    expect($('.has-error').is(':visible')).toBeTruthy()
  })
})
