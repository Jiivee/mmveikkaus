$(document).ready(function() {
    $('#bet-button').click(function () {
        var errors = 0;

        var radioInputs = []
        $('input:radio').each(function () {
            var rinput = $(this).attr('name');
            if ($.inArray(rinput, radioInputs) == -1) radioInputs.push(rinput);
        });        
        $.each(radioInputs, function (i, input) {
            if ($('input[name="' + input + '"]:checked').length == 0) {
                $('#label1-' +input).addClass('radio-unchecked');
                $('#labelx-' +input).addClass('radio-unchecked');
                $('#label2-' +input).addClass('radio-unchecked');
                errors++;
            }
        });    

        var textInputs = []
        $('input:text').each(function () {
            var tinput = $(this).attr('name');
            if ($.inArray(tinput, textInputs) == -1) textInputs.push(tinput);
        });

        $.each(textInputs, function (i, input) {
            if ($('input[name="' + input + '"]').val() === '') {
                $('#match-bet-' + input).addClass('bet-goals-missing');
                errors++;
            }
        });

        if (errors === 0) {
            $('#match-bet-form').submit();
        }
    });


    $('.radio-button').click(function () {
        var id = $(this).attr('id').split('-')[1];
        if ($('#label1-' +id).hasClass('radio-unchecked')) {
            $('#label1-' +id).removeClass('radio-unchecked');
            $('#labelx-' +id).removeClass('radio-unchecked');
            $('#label2-' +id).removeClass('radio-unchecked');            
        }
    });

    $(".bet-goals").on("input", function() {
        var id = $(this).attr('id');
        if ($('#'+id).hasClass('bet-goals-missing')) {
            $('#'+id).removeClass('bet-goals-missing');
        }
    });


});

function validate(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode( key );
    var regex = /[0-9]/;
    if( !regex.test(key) ) {
        theEvent.returnValue = false;
        if(theEvent.preventDefault) theEvent.preventDefault();
    }
}


