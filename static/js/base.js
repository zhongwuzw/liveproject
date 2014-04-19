jQuery(function(){
	setInterval("update()",60000);
	}
);

function update(){
	most_recent = $('#update-holder').find('div:first');
	$.getJSON('/updates-after/' + most_recent.attr('id') + '/', 
		function(data) {
		cycle_class = most_recent.hasClass("odd") ? "even" : "odd";
		jQuery.each(data, function() {
			$('#update-holder').prepend('<div id="' + this.pk + 
				'" class="update ' + cycle_class + '"><div class="timestamp">' + this.fields.timestamp +
				'</div><div class="text">' + this.fields.text + '</div><div class="clear"></div></div>');
			cycle_class = (cycle_class == "odd") ? "even" : "odd";

		});
			
	});
}