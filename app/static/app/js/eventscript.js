
$('.event-like').click(function(){
    let id=$(this).attr("pid").toString();
    let heartIcon= $(this).find('.heart-icon');
    heartIcon.toggleClass('clicked');
    // let elm=this.parentNode.children[2];
    $.ajax(
        {
            type:"GET",
            url: "/eventliked",
            data:{
                event_id: id
            },
            success: function(data){
                console.log(data.msg);
            }
            
           
        }
   
    )
});

// const heartIcon = document.querySelector('.heart-icon');

//         heartIcon.addEventListener('click', function() {
//             // Toggle the 'clicked' class when the icon is clicked
//             this.classList.toggle('liked');
//         });


// $('.event-like').click(function(){
//    let heartIcon= $(this).find('.heart-icon');
//    heartIcon.toggleClass('clicked');
//     // let elm=this.parentNode.children[2];
   
// });

// $(document).ready(function() {
//     $('.heart-icon').click(function() {
//         // Toggle the 'clicked' class when the icon is clicked
//         $(this).toggleClass('clicked');
//     });
// });
