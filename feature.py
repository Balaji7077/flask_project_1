from flask import Flask

FAI=Flask(__name__)
@FAI.route('/stringresponse')
def stringresponse():
    return 'hai this is our secondstringresponse view of flask'
if __name__=='__main__':
    FAI.run(debug=True)

    