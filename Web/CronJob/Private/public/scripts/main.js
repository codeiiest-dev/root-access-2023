const socket = io();

socket.on('update flag', (char) => {
  const flagContainer = document.getElementById('flag');
  flagContainer.innerText = `Here is a part of your flag : ${char}`;
});