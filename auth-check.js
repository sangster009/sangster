(function() {
  if (typeof localStorage === "undefined") return;
  if (localStorage.getItem("sangster-auth") !== "1") {
    window.location.replace("index.html");
  }
})();
