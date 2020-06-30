# Multistage build requires Docker 17.05 or higher

# build
FROM node:lts-alpine as build-stage

ENV USER=dorian
ENV UID=1000
ENV GID=1000

RUN apk update --no-cache && \
    apk add --no-cache \
    bash \
    npm && \
    npm i -g @vue/cli && \
    deluser node && \
    addgroup --gid "$GID" "$USER" && \
    adduser \
    --disabled-password \
    --gecos "" \
    --ingroup "$USER" \
    --uid "$UID" \
    "$USER" 

EXPOSE 8080

WORKDIR /app
COPY ./vue_app/package*.json ./
RUN npm install
COPY ./vue_app/ ./
RUN npm run build

# production
FROM nginx:1.16.1-alpine
COPY --from=build-stage /app/dist /var/www/vue_app
COPY ./nginx/ /etc/nginx/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]