import requests
from django.shortcuts import render

def find_cves(request):
    nvd_api_url = 'https://services.nvd.nist.gov/rest/json/cves/1.0'
    params = {
        'startIndex': 0,
        'resultsPerPage': 100,
        'modStartDate': '2023-01-01T00:00:00:000 UTC-05:00',
        'modEndDate': '2023-06-01T00:00:00:000 UTC-05:00'
    }

    response = requests.get(nvd_api_url, params=params)
    cves = response.json()

    cve_list = []
    for cve in cves['result']['CVE_Items']:
        cve_id = cve['cve']['CVE_data_meta']['ID']
        description = cve['cve']['description']['description_data'][0]['value']
        cve_list.append({'id': cve_id, 'description': description})

    context = {'cves': cve_list}
    return render(request, 'cve/cve_list.html', context)
