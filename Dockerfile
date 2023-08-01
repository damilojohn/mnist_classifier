FROM public.ecr.aws/lambda/python:3.9


RUN pip install -r requirements.txt 

COPY app ./ 

#set entry point 
CMD ["lambda_predict.lambda_handler"]
