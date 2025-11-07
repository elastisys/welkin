# Quick Setup (Not for Production)

>[!WARNING]
> This is a mock for brainstorming purposes.
> Nothing here is expected to work.

This page allows you to quick set up Welkin Apps to "kick the tires".

## Requirements

A laptop or VM running Ubuntu 24.04 with 8 CPUs and 16 GB of RAM.


## Setup

Create two kind clusters:

```shell
kind create cluster --name sc
kind create cluster --name wc
```

## Download, Configure and Install Welkin Apps

```
# Download Welkin Apps
git clone git@github.com:elastisys/compliantkubernetes-apps/
cd compliantkubernetes-apps

# Configure Welkin Apps
mkdir .config  # This creates the config folder
export CK8S_CONFIG_PATH=.config
./bin/ck8s init --flavor quick-setup

# Install Welkin Apps
./bin/ck8s apply
```

You should see an output along the lines of:

```
Welkin Apps installed successfully!

To try out Welkin as an application developer:

- Go to https://grafana.welkin.test for Metrics.
- Go to https://opensearch.welkin.test for Logs.
- Go to https://harbor.welkin.test for Container registry.

The KUBECONFIG for application developers can be found at: ./.config/kubeconfig

The following static application developer account was created:

- Username: appdev
- Password: 983j4oim2l3kj4swer

Happy hacking!
```

## Download and Install user-demo

```
export DOMAIN=welkin.test
```

Then follow the instruction in the [application developer](...) section.

Finally, you can check:

- The endpoint of the application: <https://myapp.welkin.test>.
- The logs of the application: <https://opensearch.welkin.test>.
- The metrics of the application: <https://grafana.welkin.test>.

### Limitations

Being a non-production deployment, the following limitations apply:

- Not HA
- Falco doesn't work
- ...

## Basic Configuration

> [!NOTE]
> This is a local-only form. No data will be sent to any servers.

Input the following information to generate a basic Welkin Apps configuration.

<div style="
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 8px 12px;
  align-items: center;
  max-width: 600px;
  padding: 20px 24px;
  border: 1px dashed var(--elastisys-sky-blue-dark);
  border-radius: 1px;
">
  <label for="objectStorage.s3.regionEndpoint">Object storage URL:</label>
  <input id="objectStorage.s3.regionEndpoint" type="text" placeholder="https://s3.mycorp.test" />

  <label for="objectStorage.s3.accessKey">Object storage access key:</label>
  <input id="objectStorage.s3.accessKey" type="text" placeholder="AKIAIOSFODNN7EXAMPLE" />

  <label for="objectStorage.s3.secretKey">Object storage secret key:</label>
  <input id="objectStorage.s3.secretKey" type="text" placeholder="EXAMPLESECRETKEY" />
</div>

### Welkin Apps Configuration

Place the files generated below in the `.config` folder you created above.

<pre id="sc-config.yaml">
</pre>

<script>
function genConfig() {
  const regionEndpoint = document.getElementById('objectStorage.s3.regionEndpoint').value;
  const accessKey = document.getElementById('objectStorage.s3.accessKey').value;
  const secretKey = document.getElementById('objectStorage.s3.secretKey').value;

  document.getElementById('sc-config.yaml').innerHTML = `# sc-config.yaml
objectStorage:
  type: s3
  regionEndpoint: ${regionEndpoint}
  accessKey: ${accessKey}
  secretKey: ${secretKey}
`;
}

for (const i of [
  'objectStorage.s3.regionEndpoint',
  'objectStorage.s3.accessKey',
  'objectStorage.s3.secretKey',
]) {
  const el = document.getElementById(i);
  console.log('Adding listener', i, el);
  el.addEventListener("input", (event) => { genConfig(); })
}
genConfig();
</script>
