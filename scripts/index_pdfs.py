import requests

def upload_pdf_to_solr(pdf_path, doc_id):
    url = f'http://localhost:8983/solr/pdf_core/update/extract?literal.id={doc_id}&commit=true'
    with open(pdf_path, 'rb') as file:
        response = requests.post(url, files={'file': file})
    
    try:
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print(f'Response content: {response.text}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
        print(f'Response content: {response.text}')
    except ValueError as json_err:
        print(f'JSON decode error occurred: {json_err}')
        print(f'Response content: {response.text}')

if __name__ == "__main__":
    pdf_path = 'llm.pdf'  # Adjust the path if necessary
    doc_id = 'doc1'
    response = upload_pdf_to_solr(pdf_path, doc_id)
    print(response)
