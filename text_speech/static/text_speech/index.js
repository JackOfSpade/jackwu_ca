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
  var speech = $("#speech");
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

  $("#text_speech_form").on("submit", function(event){
    speech.hide();
    speech.prop("disabled", true);
    loading.show();

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
          alert(response["return_text"])

          let $audio = $('<audio />', { src: "/jackwu_ca/speech.mp3" });
          $audio[0].play();
          loading.hide();
          speech.prop("disabled", false);
          speech.show();
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

