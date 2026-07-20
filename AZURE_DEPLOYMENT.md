# Python Calculator - Azure App Service Deployment Guide

## Prerequisites
- Azure Account ([Sign up free](https://azure.microsoft.com/free/))
- Azure CLI installed (`az` command)
- Git

## Deployment Steps

### Option 1: Deploy via Azure CLI (Recommended)

1. **Login to Azure**
   ```bash
   az login
   ```

2. **Create a Resource Group**
   ```bash
   az group create --name myCalcGroup --location eastus
   ```

3. **Create an App Service Plan**
   ```bash
   az appservice plan create --name myCalcPlan --resource-group myCalcGroup --sku B1 --is-linux
   ```

4. **Create a Web App**
   ```bash
   az webapp create --resource-group myCalcGroup --plan myCalcPlan --name my-calculator-app --runtime "PYTHON|3.11"
   ```

5. **Deploy from GitHub**
   ```bash
   az webapp deployment source config-zip --resource-group myCalcGroup --name my-calculator-app --src <path-to-zip>
   ```

### Option 2: Deploy via Azure Portal

1. Go to [Azure Portal](https://portal.azure.com)
2. Create new **Web App**
3. Select **Python 3.11** as Runtime Stack
4. Go to **Deployment Center** → Configure GitHub (connect repository)
5. Select your branch (`main`)
6. Azure will auto-deploy on every push

### Option 3: Deploy Using GitHub Actions

Create `.github/workflows/azure-deploy.yml`:

```yaml
name: Deploy to Azure

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'my-calculator-app'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
```

## Environment Setup

For a CLI-based app, you may want to create a web interface. Here are options:

### Simple Flask Web Wrapper

Create `app.py`:
```python
from flask import Flask, render_template, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>Calculator</h1>
        <form method="POST" action="/calculate">
            <input type="number" name="num1" required>
            <select name="op">
                <option>+</option>
                <option>-</option>
                <option>*</option>
                <option>/</option>
            </select>
            <input type="number" name="num2" required>
            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
```

Then update `requirements.txt` to include Flask:
```
Flask==2.3.0
```

## Monitoring & Logs

View logs from Azure:
```bash
az webapp log tail --resource-group myCalcGroup --name my-calculator-app
```

## Cost
- **B1 Plan**: ~$12/month (1 GB RAM, shared compute)
- **Always Free Tier**: Available for testing

## Useful Links
- [Python on App Service Docs](https://learn.microsoft.com/azure/app-service/quickstart-python)
- [Deploy Python Web App](https://learn.microsoft.com/azure/app-service/quickstart-python-ubunutu-web-app)
