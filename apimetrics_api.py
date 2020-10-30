import requests

class APImetricsAPI:

    BASE_URL = "https://client.apimetrics.io/api/2"
    GET_HEADERS = {"Accept": "application/json"}
    POST_HEADERS = {"Content-Type": "application/json", **GET_HEADERS}

    def __init__(self, api_key):
        self.api_key = api_key
        self._auths = None
        self._tokens = None
        self._calls = None
        self._workflows = None
        self._auths_by_tag = None
        self._tokens_by_auth = None
        self._calls_by_tag = None
        self._workflows_by_tag = None
        
    @property
    def auths(self):
        if self._auths is None:
            self._auths = { obj['id']: obj for obj in self.get_auths().get('results', []) }
            print(f'Found {len(self._auths)} Auths')
        return self._auths
    
    @property
    def auths_by_tag(self):
        if self._auths_by_tag is None:
            self._auths_by_tag = {}
            for auth in self.auths.values():
                for tag in auth['meta']['tags']:
                    if ':' in tag:
                        self._auths_by_tag[tag] = auth['id']
            print(f'Auth tags: {", ".join(self._auths_by_tag.keys())}')
        return self._auths_by_tag
    
    @property
    def tokens(self):
        if self._tokens is None:
            self._tokens = { obj['id']: obj for obj in self.get_tokens().get('results', []) }
            print(f'Found {len(self._tokens)} Tokens')
        return self._tokens
    
    @property
    def tokens_by_auth(self):
        if self._tokens_by_auth is None:
            self._tokens_by_auth = {}
            for token in self.tokens.values():
                auth_id = token['meta']['auth_id']
                self._tokens_by_auth[auth_id] = token['id']
            print(f'Tokens for auths: {", ".join(self.auths.get(auth, {}).get("meta", {}).get("name", auth) for auth in self._tokens_by_auth.keys())}')
        return self._tokens_by_auth
    
    @property
    def calls(self):
        if self._calls is None:
            self._calls = { obj['id']: obj for obj in self.get_calls().get('results', []) }
            print(f'Found {len(self._calls)} Calls')
        return self._calls

    @property   
    def calls_by_tag(self):
        if self._calls_by_tag is None:
            self._calls_by_tag = {}
            for call in self.calls.values():
                for tag in call['meta']['tags']:
                    if ':' in tag:
                        self._calls_by_tag[tag] = call['id']
            print(f'Call tags: {", ".join(self._calls_by_tag.keys())}')
        return self._calls_by_tag
    
    @property
    def workflows(self):
        if self._workflows is None:
            self._workflows = { obj['id']: obj for obj in self.get_workflows().get('results', []) }
            print(f'Found {len(self._workflows)} Workflows')
        return self._workflows
    
    @property   
    def workflows_by_tag(self):
        if self._workflows_by_tag is None:
            self._workflows_by_tag = {}
            for workflow in self.workflows.values():
                for tag in workflow['meta']['tags']:
                    if ':' in tag:
                        self._workflows_by_tag[tag] = workflow['id']
            print(f'Call tags: {", ".join(self._workflows_by_tag.keys())}')
        return self._workflows_by_tag
        
    def headers(self, is_post=False):
        other_headers = self.POST_HEADERS if is_post else self.GET_HEADERS
        return {"Authorization": "Bearer {}".format(self.api_key), **other_headers}

    def get(self, path, params):
        resp = requests.get(
            "{}/{path}".format(self.BASE_URL, path=path),
            headers=self.headers(),
            params=params,
        )
        try:
            resp.raise_for_status()
        except Exception as ex:
            print(resp.content)
            raise ex
        return resp.json()

    def post(self, path, setup):
        resp = requests.post(
            "{}/{path}".format(self.BASE_URL, path=path),
            json=setup,
            headers=self.headers(True),
        )
        try:
            resp.raise_for_status()
        except Exception as ex:
            print(resp.content)
            raise ex
        return resp.json()
    
    def delete(self, path):
        resp = requests.delete(
            "{}/{path}".format(self.BASE_URL, path=path),
            headers=self.headers(),
        )
        try:
            resp.raise_for_status()
        except Exception as ex:
            print(resp.content)
            raise ex
        return True
    
    def get_all(self, path):
        cursor = None
        more = True
        results = []
        while more:
            resp = self.get(path, {'cursor': cursor})
            results.extend(resp.get('results', []))
            more = resp['meta']['more']
            cursor = resp['meta']['next_cursor']
        resp['results'] = results
        return resp

    def get_auths(self):
        return self.get_all("auth/")

    def get_calls(self):
        return self.get_all("calls/")

    def get_schedules(self):
        return self.get_all("schedules/")

    def get_tokens(self):
        return self.get_all("tokens/")

    def get_token(self, id_str):
        return self.get("tokens/{}".format(id_str))

    def get_tokens_for_auth(self, auth_id):
        return self.get("tokens/auth/{}/".format(auth_id))

    def get_workflows(self):
        return self.get_all("workflows")

    def create_auth(self, setup):
        self._auths = None
        self._auths_by_tag = None
        return self.post("auth/", setup)

    def create_call(self, setup):
        self._calls = None
        self._calls_by_tag = None
        return self.post("calls/", setup)
    
    def set_call_conditions(self, call_id, setup):
        return self.post("calls/{}/conditions/".format(call_id), setup)

    def create_token(self, setup):
        self._tokens = None
        self._tokens_by_auth = None
        return self.post("tokens/", setup)

    def create_workflow(self, setup):
        self._workflows = None
        self._workflows_by_tag = None
        return self.post("workflows/", setup)

    def update_auth(self, id_str, setup):
        return self.post("auth/{}/".format(id_str), setup)

    def update_call(self, id_str, setup):
        return self.post("calls/{}/".format(id_str), setup)

    def update_token(self, id_str, setup):
        return self.post("tokens/{}/".format(id_str), setup)

    def update_workflow(self, id_str, setup):
        return self.post("workflows/{}/".format(id_str), setup)

    def delete_auth(self, id_str):
        self._auths = None
        self._auths_by_tag = None
        return self.delete("auth/{}/".format(id_str))

    def delete_call(self, id_str):
        self._calls = None
        self._calls_by_tag = None
        return self.delete("calls/{}/".format(id_str))

    def delete_token(self, id_str):
        self._tokens = None
        self._tokens_by_auth = None
        return self.delete("tokens/{}/".format(id_str))

    def delete_workflow(self, id_str):
        self._workflows = None
        self._workflows_by_tag = None
        return self.delete("workflows/{}/".format(id_str))
    
    def get_env_variable(self, env, key):
        return self.get("environment/{env}/{key}".format(env=env, key=key))

    def set_env_variable(self, env, key, val):
        return self.post(
            "environment/{env}/{key}".format(env=env, key=key), {"value": val}
        )

    def run_call(self, id_str, config):
        return self.post("calls/{}/run".format(id_str), config)
