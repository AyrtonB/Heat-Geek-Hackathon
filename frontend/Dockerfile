# Use a Node.js image to build the application
FROM node:alpine AS build

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy all files from the host to the container's working directory
COPY . .

# Install dependencies and build the project
RUN yarn install --frozen-lockfile --production \
  && yarn run build

# Use a smaller base image for the final image
FROM node:alpine

# Install 'serve' globally
RUN npm install -g serve

# Set the working directory for the serve command
WORKDIR /usr/src/app

# Copy the built files from the previous stage
COPY --from=build /usr/src/app/build/ .

# Expose port 8080
EXPOSE 8080

# Use 'serve' to serve the static files on port 8080
CMD ["serve", "-l", "8080"]
