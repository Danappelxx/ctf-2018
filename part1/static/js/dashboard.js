function showDate() {
	function pad2(string) {
		return String("00" + string).slice(-2);
	}

	var now = new Date();
	document.getElementById("time").innerHTML = pad2(now.getHours()) + ":" + pad2(now.getMinutes()) + ":" + pad2(now.getSeconds());
}
showDate();
setInterval(showDate, 1000);

function Calculator($container) {
	var self = this;
	self.$container = $container;
	self.$input = self.$container.find("input");
	self.$buttons = self.$container.find(".calc-button");

	self.$buttons.click(function() {
		var $button = $(this);
		var operation = $button.text();

		if (operation === "=") {
			self.processInput();
		} else if (operation == "c") {
			self.$input.val("");
		} else {
			self.$input.val(self.$input.val() + operation);
		}
	});

	self.processInput = function() {
		// sends input to server and outputs result
		var input = self.$input.val();
		var expression = "print(" + input + ")";
		var data = JSON.stringify({ "input": expression });
		console.log(data);
		$.ajax({
			type: "POST",
			url: "/calculate",
			data: data,
			contentType: "application/json",
			success: function(response) {
				window.response = response;
				self.$input.val(response);
			}
		});
	}
}

var calculator = new Calculator($("#calculator"));
