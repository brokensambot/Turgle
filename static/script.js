// Copyright (c) 2011 Sam White
//
// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish,
// distribute, sublicense, and/or sell copies of the Software, and to
// permit persons to whom the Software is furnished to do so, subject to
// the following conditions:
//
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
// LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
// OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
//

var answersLimit;
var timer;

$(document).ready(function() {
    $('#settings').click(showMenu);
    $('#access').click(clearAccess);
    $('#secret').click(clearSecret);
    $('#access').focusout(fillAccess);
    $('#secret').focusout(fillSecret);
    $('#search').click(startSearch);
    $('#lucky').click(startSearch);
});

function showMenu(e) {
    $('#settings').css({'background-color':'#ffffff',
                        'background-image':'url(\'dark-gear.png\')',
                        'border-left':'1px solid #c0c0c0',
                        'border-right':'1px solid #c0c0c0',
                        'color':'#2d2d2d',
                        'right':'4px'});
    $('#menu').css({'visibility':'visible'});
    $('#settings').unbind();
    setTimeout(function() {$(document).click(hideMenu);}, 0);
}

function hideMenu(e) {
    var node = e.target;
    while(node != document) {
        if (node == $('#menu')[0])
            return;
        node = node.parentNode;
    }
    $('#settings').css({'background-color':'#2d2d2d',
                        'background-image':'url(\'light-gear.png\')',
                        'border':'none',
                        'color':'#cccccc',
                        'right':'5px'});
    $('#menu').css({'visibility':'hidden'});
    $(document).unbind();
    setTimeout(function() {$('#settings').click(showMenu);}, 0);
}

function clearAccess(e) {
    var node = $(e.target);
    if (node.val() == 'AWS Access Key') {
        node.val('');
        node.css({'color':'#2d2d2d'});
    }
}

function clearSecret(e) {
    var node = $(e.target);
    if (node.val() == 'AWS Secret Key') {
        node.val('');
        node.css({'color':'#2d2d2d'});
    }
}

function fillAccess(e) {
    var node = $(e.target);
    if (node.val() == '') {
        node.val('AWS Access Key');
        node.css({'color':'#c0c0c0'});
    }
}

function fillSecret(e) {
    var node = $(e.target);
    if (node.val() == '') {
        node.val('AWS Secret Key');
        node.css({'color':'#c0c0c0'});
    }
}

function startSearch(e) {
    clearInterval(timer);
    $('.answer').fadeOut(100, function() {$(this).remove();});
    if (e.target == $('#lucky')[0])
        answersLimit = 1;
    else
        answersLimit = 10;
    postQuestion();
    timer = setInterval(function() {updateSearch();}, 5000);
}

function updateSearch() {
    var answers = getAnswers();
    if (answers.length == answersLimit) {
        clearInterval(timer);
    }
    for (var i = $('.answer').length; i < answers.length; i++) {
        var node = $('<p class="answer">' + answers[i] + '</p>');
        $('body').append(node.hide().fadeIn(100));
    }
}

function postQuestion() {
    /* Post question here. */
}

function getAnswers() {
    /* Get answers here. */
    
    /* Begin testing. */
    return ['White', 'Pink', 'Red', 'Orange', 'Brown', 'Yellow', 'Gray', 'Green', 'Cyan', 'Blue'];
    /* End testing. */
}
