var fetchWorkResults = function() {
    searchPageCallback('work', 1, '#works');
};

var fetchElementResults = function() {
    searchPageCallback('element', 1, '#elements');
};

var searchPageCallback = function(searchtype, page, target) {
    var qstr = window.location.search.replace("?", "");
    if (searchtype == 'work') {
        if (window.location.search.match(/wpage/g) === null) {
            qstr = qstr + "&wpage=" + page;
        }
    }

    if (searchtype == 'element') {
        if (window.location.search.match(/epage/g) === null) {
            qstr = qstr + "&epage=" + page;
        }
    }

    $.ajax({
        url: '/search/results/' + searchtype,
        data: qstr,
        success: function(data) {
            $(target).empty();
            $(target).append(data);
        }
    });
};

var worksPagerActions = function() {
    $('.works-next, .works-prev').on({
        'click': function(event) {
            searchPageCallback('work', $(this).attr('target'), '#works');
            return false;
        }
    });
};

var elementsPagerActions = function() {
    $('.elements-next, .elements-prev').on({
        'click': function(event) {
            searchPageCallback('element', $(this).attr('target'), '#elements');
            return false;
        }
    });
};