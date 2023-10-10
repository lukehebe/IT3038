const http = require('http');
const os = require('os');

const server = http.createServer((req, res) => {
  
  res.setHeader('Content-Type', 'text/html');
  const hostname = os.hostname();
  const ip = getIpAddress();

 
  const uptime = getUptime();

  const totalMemory = Math.round(os.totalmem() / (1024 * 1024)); // Convert to MB
  const freeMemory = Math.round(os.freemem() / (1024 * 1024)); // Convert to MB
  const numCPUs = os.cpus().length;

  const htmlResponse = `
    <h1>Server Information</h1>
    <p>Hostname: ${hostname}</p>
    <p>IP Address: ${ip}</p>
    <p>Server Uptime: ${uptime}</p>
    <p>Total Memory: ${totalMemory} MB</p>
    <p>Free Memory: ${freeMemory} MB</p>
    <p>Number of CPUs: ${numCPUs}</p>
  `;
  res.end(htmlResponse);
});


const port = 3000;

server.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/`);
});

function getIpAddress() {
  const interfaces = os.networkInterfaces();
  for (const key of Object.keys(interfaces)) {
    for (const entry of interfaces[key]) {
      if (!entry.internal && entry.family === 'IPv4') {
        return entry.address;
      }
    }
  }
  return 'Not Found';
}

function getUptime() {
  const uptimeInSeconds = os.uptime();
  const days = Math.floor(uptimeInSeconds / (3600 * 24));
  const hours = Math.floor((uptimeInSeconds % (3600 * 24)) / 3600);
  const minutes = Math.floor((uptimeInSeconds % 3600) / 60);
  const seconds = Math.floor(uptimeInSeconds % 60);
  return `${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds`;
}
