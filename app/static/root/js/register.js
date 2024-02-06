$(document).ready(function(){

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;

    setProgressBar(current);

    $(".next").click(function(){
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        // Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

        // Show the next fieldset
        next_fs.show();
        // Hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // For making fieldset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({'opacity': opacity});
            },
            duration: 500
        });
        setProgressBar(++current);
    });

    $(".previous").click(function(){
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();

        // Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

        // Show the previous fieldset
        previous_fs.show();

        // Hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // For making fieldset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({'opacity': opacity});
            },
            duration: 500
        });
        setProgressBar(--current);
    });

    function setProgressBar(curStep){
        var percent = parseFloat(100 / steps) * curStep;
        percent = percent.toFixed();
        $(".progress-bar").css("width",percent+"%");
    }

    $("#msform").submit(function(e) {
        e.preventDefault(); // Prevent the form from submitting normally
        
        // Check if all required fields are filled
        var allFieldsFilled = true;
        $("input[required]").each(function() {
            if ($(this).val() === "") {
                allFieldsFilled = false;
                return false; // Exit the loop early if any required field is empty
            }
        });

        if (!allFieldsFilled) {
            alert("Please fill in all required fields before submitting.");
            return;
        }
        
        // Display success message
        $(".form-card").hide(); // Hide the form fields
        $("#progressbar").hide(); // Hide the progress bar
        $(".steps").hide(); // Hide step indicators
        $("#heading").text("SUCCESS!"); // Change heading text
        $(".fit-image").attr("src", "../../static/root/img/Confirm.png"); // Change image source
        $(".purple-text").text("You Have Successfully Registered for 2024 WAEC"); // Change success message
    });

});
