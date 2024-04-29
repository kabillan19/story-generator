// $(document).ready(function() {
//     $("#story-form").submit(function(event) {
//         event.preventDefault();
//         var prompt = $("#prompt").val();

//         $.ajax({
//             type: "POST",
//             url: "/generate-story",
//             contentType: "application/json",
//             data: JSON.stringify({ prompt: prompt }),
//             success: function(response) {
//                 $("#story-output").text(response.story);
//             },
//             error: function(xhr, status, error) {
//                 console.error("Error:", error);
//             }
//         });
//     });
// });
