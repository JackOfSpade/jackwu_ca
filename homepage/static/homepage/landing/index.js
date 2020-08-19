$(document).ready(function() {
    window.addEventListener("touchmove", function (event) {
        event.preventDefault();
    }, false);

    if (typeof window.devicePixelRatio != 'undefined' && window.devicePixelRatio > 2) {
        var meta = document.getElementById("viewport");
        meta.setAttribute('content', 'width=device-width, initial-scale=' + (2 / window.devicePixelRatio) + ', user-scalable=no');
    }

    //Google Analytics
    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o), m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-54755897-1', 'auto');
    ga('send', 'pageview');

    lime.embed("content", 0, 0, "FFFFFF");

    function initialize(speed) {
        // Animation for button 1
        window.setTimeout(function () {
            $(".weather_button").animate({
                top: "32vh",
                left: "33vw"
            }, speed);
            // After animation is done
            window.setTimeout(function () {
                $(".weather_button").hover(function () {
                    $(this).animate({
                        opacity: "1"
                    });
                }, function () {
                    $(this).animate({
                        opacity: "0.3"
                    });
                });
            }, speed);
        }, 0);

        // Animation for button 2
        window.setTimeout(function () {
            $(".stock_button").animate({
                top: "22vh"
            }, speed);
            // After animation is done
            window.setTimeout(function () {
                $(".stock_button").hover(function () {
                    $(this).animate({
                        opacity: "1"
                    });
                }, function () {
                    $(this).animate({
                        opacity: "0.3"
                    });
                });
            }, speed);
        }, speed * 1 * 0.25);

        // Animation for button 3
        window.setTimeout(function () {
            $(".crime_button").animate({
                top: "32vh",
                right: "33vw"
            }, speed);
            // After animation is done
            window.setTimeout(function () {
                $(".crime_button").hover(function () {
                    $(this).animate({
                        opacity: "1"
                    });
                }, function () {
                    $(this).animate({
                        opacity: "0.3"
                    });
                });
            }, speed);
        }, speed * 2 * 0.25);

        // Animation for button 4
        window.setTimeout(function () {
            $(".review_button").animate({
                bottom: "32vh",
                right: "33vw"
            }, speed);
            // After animation is done
            window.setTimeout(function () {
                $(".review_button").hover(function () {
                    $(this).animate({
                        opacity: "1"
                    });
                }, function () {
                    $(this).animate({
                        opacity: "0.3"
                    });
                });
            }, speed);
        }, speed * 3 * 0.25);

        // Animation for button 5
        window.setTimeout(function () {
            $(".under_construction1").animate({
                bottom: "17vh"
            }, speed);
            // After animation is done
            window.setTimeout(function () {
                $(".under_construction1").hover(function () {
                    $(this).animate({
                        opacity: "1"
                    });
                }, function () {
                    $(this).animate({
                        opacity: "0.3"
                    });
                });
            }, speed);
        }, speed * 4 * 0.25);

        // Animation for button 6
        window.setTimeout(function () {
            $(".under_construction2").animate({
                bottom: "32vh",
                left: "33vw"
            }, speed);
            // After animation is done
            window.setTimeout(function () {
                $(".under_construction2").hover(function () {
                    $(this).animate({
                        opacity: "1"
                    });
                }, function () {
                    $(this).animate({
                        opacity: "0.3"
                    });
                });
            }, speed);
        }, speed * 5 * 0.25);
    }

    $(document).tooltip({
        track: true,
        show: {
            delay: 0
        },
        hide: {
            delay: 0
        }
    });

    //Session is reset on tab close.
    if (sessionStorage.getItem('dontLoad') == null)
    {
         // After text is gone
        $("#content").one("click", function () {
            // Wait a moment after first click
            window.setTimeout(function () {
                initialize(4500)
            }, 1500);
        });

        sessionStorage.setItem("dontLoad", "true");
    }
    else
    {
        $(".animated_text").remove();
        initialize(0)
    }

    // $(".stock_button, .crime_button").click(function(){
    //     $("body").fadeOut()
    // });

    // $(".weather_button").click(function(){
    //     var base_url = window.location.origin;
    //     location.href = base_url + "/weather/";
    // });

    $(".stock_button").click(function () {
        var base_url = window.location.origin;
        $("body").fadeOut("slow", function(){
            location.href = base_url + "/analysis/stock/";
        })
    });

    $(".crime_button").click(function () {
        var base_url = window.location.origin;
        $("body").fadeOut("slow", function(){
            location.href = base_url + "/analysis/crime/";
        })
    });

    // $(".review_button").click(function(){
    //     var base_url = window.location.origin;
    //     location.href = base_url + "/ML_reviews/";
    // });

    //  $(".under_construction1").click(function(){
    //     var base_url = window.location.origin;
    //     location.href = base_url + "";
    // });

    // $(".under_construction2").click(function () {
    //     var base_url = window.location.origin;
    //     location.href = base_url + "";
    // });
});
