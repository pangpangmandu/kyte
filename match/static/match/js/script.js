$(window).on("load", function(){
    $(".loader").fadeOut(750);

    $(".items").isotope({
        filter: '*',
        animationOptions: {
            duration: 1500,
            easing: 'linear',
            queue: false
        }
    });
})


$(document).ready(function(){
    $('#slides').superslides({
        animation: 'fade',
        play: 3000,
        pagination: false,
        inherit_height_from: '#slides',
        inherit_width_from: '#slides'
    });

    var typed = new Typed(".typed", {
        strings: ["Are you tired of finding your game friends?.", "We got you!", "100+ Steam games supported", "Enjoy the best matching service ever!"],
        typeSpeed: 70,
        loop: true,
        startDelay: 1000,
        showCursor: false
    });

    $('.owl-carousel').owlCarousel({
        loop:true,
        items: 4,
        responsive:{
            0:{
                items:1
            },
            480:{
                items:2
            },
            768:{
                items:5
            },
            938:{
                items:4
            },
        }
    });



    const firstAnniversary = new Date("March 1, 2018 00:00:00").getTime();
    const secondAnniversary = new Date("March 1, 2020 00:00:00").getTime();
    var d1, d2;
    var kooBDay = [10, 12];
    var leeBDay = [3, 9];

    //1초마다 갱신되도록 함수 생성,실행
    const x = setInterval(function() {
        const now = new Date().getTime();       // 오늘 날짜 등록
        const distanceFirst = now - firstAnniversary;     // 종료일자에서 현재일자를 뺀 시간
        const distanceSecond = secondAnniversary - now;
        d1 = Math.floor(distanceFirst / (1000 * 60 * 60 * 24));
        d2 = Math.floor(distanceSecond / (1000 * 60 * 60 * 24));

        $('.firstAnniv').text(d1);
        $('.secondAnniv').text(d2);

        var today = new Date();
        var lbday = new Date(today.getFullYear(), leeBDay[1]-1, leeBDay[0]);
        var kbday = new Date(today.getFullYear(), kooBDay[1]-1, kooBDay[0]);

        if( today.getTime() > lbday.getTime()) {
            lbday.setFullYear(lbday.getFullYear()+1);
        }

        if( today.getTime() > kbday.getTime()) {
            kbday.setFullYear(kbday.getFullYear()+1);
        }

        var ldiff = lbday.getTime()-today.getTime();
        var ldays = Math.floor(ldiff/(1000*60*60*24));

        var kdiff = kbday.getTime()-today.getTime();
        var kdays = Math.floor(kdiff/(1000*60*60*24));

        $('.leeBirth').text(ldays);
        $('.kooBirth').text(kdays);
    });


    $("[data-fancybox]").fancybox({
        animationEffect: "zoom-in-out",
        hideScrollbar: false
    });



    $("#filters a").click(function() {

        $("#filters .current").removeClass("current");
        $(this).addClass("current");

        var selector = $(this).attr("data-filter");

        $(".items").isotope({
            filter: selector,
            animationOptions: {
                duration: 1500,
                easing: 'linear',
                queue: false
            }
        });

        return false;
    });


    $("#navigation li a").click(function(e) {       // 'e' means click event itself
        e.preventDefault();                         // when click event occurs, don't do default action(teleporting to link)

        var targetElement = $(this).attr("href");      // href contains the link of each id section (#skills, #video, #photos)
        var targetPosition = $(targetElement).offset().top;     // get the top position of each section
        $("html, body").animate({ scrollTop: targetPosition - 50 }, "slow");
    });



    const nav = $("#navigation");           // nav will never be changed
    const navTop = nav.offset().top;        // 320

    $(window).on("scroll", stickyNavigation);           // if scroll event occurs, execute stidkyNavigation function

    function stickyNavigation() {
        const body = $("body");

        if($(window).scrollTop() >= navTop) {           // scrollTop() is the top index of current window when sroll event occurs
            body.css("padding-top", nav.outerHeight() +"px");
            body.addClass("fixedNav");
        }
        else {
            body.css("padding-top", 0);
            body.removeClass("fixedNav");
        }
    }
});

/*$(".photoLink").click(function(click){
    var target = $(click.target);

    if(!target.hasClass("item") && !target.hasClass("optionsButton")) {
        hideOptionsMenu();
    }
})*/

