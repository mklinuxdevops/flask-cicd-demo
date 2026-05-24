from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>New CI/CD Pipeline</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                text-align: center;
                background: rgba(255,255,255,0.08);
                padding: 50px;
                border-radius: 20px;
                box-shadow: 0 0 25px rgba(0,0,0,0.5);
                width: 70%;
                max-width: 700px;
            }

            h1 {
                font-size: 50px;
                margin-bottom: 20px;
                color: #38bdf8;
            }

            h2 {
                color: #22c55e;
                margin-bottom: 30px;
            }

            p {
                font-size: 20px;
                line-height: 1.8;
            }

            .pipeline {
                margin-top: 30px;
                padding: 20px;
                background: rgba(255,255,255,0.05);
                border-radius: 15px;
                font-size: 22px;
                color: #facc15;
            }

            .footer {
                margin-top: 30px;
                font-size: 16px;
                color: #cbd5e1;
            }

            .badge {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #22c55e;
                color: white;
                border-radius: 50px;
                font-weight: bold;
                font-size: 18px;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>🚀 New CI/CD Pipeline Project</h1>

            <h2>New Flask Application Deployed Successfully</h2>

            <p>
                This New application is running using:
            </p>

            <div class="pipeline">
                GitHub → Jenkins → Docker → Flask App
            </div>

            <div class="badge">
                ✅ Deployment Successful New
            </div>

            <div class="footer">
                DevOps Pipeline by Dracula MK
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
