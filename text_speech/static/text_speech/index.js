$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie("csrftoken");

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var results_table = $("#results_table")
    var speech = $("#speak");
    var loading = $("#loading");

    loading.hide();
    var speed = $("#speed");
    var handle = $("#custom-handle");

    speed.slider({
        orientation: "horizontal",
        range: "min",
        min: 0,
        max: 200,
        value: 75,
        create: function() {
            handle.text($( this ).slider("value"));
            },
        slide: function( event, ui ) {
            handle.text(ui.value);
        }
    });

    $("#id_voice").selectmenu();

    var audio = $("#audio")
    audio.hide(0)

    $("#text_speech_form").on("submit", function(event){
        speech.hide();
        speech.prop("disabled", true);
        loading.show();
        audio.hide("fast")

        //Prevent default django post behaviour for a form submission.
        event.preventDefault();

        $.ajax({
            url: "/text_speech/",
            type: "POST",
            data: {text: $("#id_text").val(),
                voice: $("#id_voice").val(),
                speed: speed.slider("option", "value")},
            dataType: "json",
            success: function (response){
                // For testing purposes:
                // alert(response["return_text"])

                audio.attr("src", response["return_text"]);
                // Cannot audio.play() without interaction because Chrome restrictions.

                loading.hide();
                speech.prop("disabled", false);
                speech.show();

                audio.show("fast")
                audio.load()
                },
            error: function(xhr,errmsg,err) {
                alert("xhr: " + xhr +
                    "\n\nerrmsg: " + errmsg +
                    "\n\nerr: " + err);

                loading.hide();
                speech.prop("disabled", false);
                speech.show();
            }
        });
    });
})

