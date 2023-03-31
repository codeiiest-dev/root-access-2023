FROM node:18-alpine

WORKDIR /app

COPY package.json .

RUN npm install
RUN apk update
RUN apk add git

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]