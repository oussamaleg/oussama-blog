$("#list").on("click",function() {
	$("#ddown").slideToggle(500)


});
$(window).click(function() {
	$("#ddown").slideUp(800);
});
$('#list').click(function(event){
    event.stopPropagation();
});
