# syntax=docker/dockerfile:1

FROM node:20-alpine AS dependencies
WORKDIR /app
COPY . .
RUN if [ -f package-lock.json ]; then npm ci; elif [ -f package.json ]; then npm install; else mkdir -p node_modules; fi

FROM node:20-alpine AS build
WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY . .
RUN if [ -f package.json ]; then npm run build; else mkdir -p dist && cp speckit.html dist/index.html; fi

FROM nginx:1.27-alpine AS runtime
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
