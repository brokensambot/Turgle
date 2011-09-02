$(document).ready(function() {
    $('#settings').click(showMenu);
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
    setTimeout(function() {$(document).click(hideMenu)}, 0);
}

function hideMenu(e) {
    var node = e.target;
    while(node != document) {
        if (node == $('#access')[0] || node == $('#secret')[0])
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
    setTimeout(function() {$('#settings').click(showMenu)}, 0);
}
