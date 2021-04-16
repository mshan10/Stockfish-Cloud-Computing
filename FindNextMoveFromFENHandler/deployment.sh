cd lambda_venv/lib/python3.8/site-packages
zip -r9 ${OLDPWD}/lambda.zip .
cd $OLDPWD
zip -g lambda.zip FindNextMoveFromFENHandler.py 
