 # Use an official Python runtime as a parent image                         
FROM python:3.7.2-slim                                                     
# Set the working directory to /app                                        
WORKDIR /app                                                               
# Copy the current directory contents into the container at /app           
COPY . /app                                                                
# Install all dependencies                                                 
RUN pip install -r requirements.txt                                        
# Expose port                                                              
EXPOSE 8000
# Change working directory
WORKDIR /app/golf_scores

