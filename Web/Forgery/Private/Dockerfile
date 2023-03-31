FROM node:18-alpine

WORKDIR /app

COPY package.json .

RUN npm install && echo "node index.js & node index1.js & node index2.js" > entrypoint.sh

COPY . .

EXPOSE 8080

CMD ["/bin/sh", "entrypoint.sh"]
