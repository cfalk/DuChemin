

function attachAnalysisClickEvents() {
    $('.view-analysis').on({
        'click': function(event) {
            ajaxRender($(this).attr('anid'));
            return false; // prevent the page from jumping when the link is clicked
        }
    });
}

function ajaxRender(anid) {
    $.ajax({
        url: '/data/analysis/' + anid,
        dataType: 'json',
        success: function(data, status, xhr) {
            $('#analysis-modal').remove();
            modal = $("<div />", {
                "id": "analysis-modal"
            }).appendTo("body");

            $("<div />", {
                "id": "analysis-modal-body"
            }).appendTo(modal);

            $("#analysis-modal-body").append(data['music']);

            var MEI = $("#meiScore");
            var cv = $('div#music canvas')[0];
            render_notation(MEI, cv, data['dimensions'][0], data['dimensions'][1]);
            $("#analysis-modal").dialog({
                'height': 500,
                'width': 920,
                'modal': true,
                'title': 'Example'
            });
        }
    });
}