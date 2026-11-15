## The Place
Infrastructure for my home and other projects at home.

> @ "the place"

📄 **The Place Lab

### The roster

| | | |
|---|---|---|
| `byss` | Old Tower | NAS · ZFS mirror · KVM host · GTX 1070 |
| `kejim` | EliteDesk 800 G2 | k3s control plane, bare metal |
| `endor` | Lemur Pro | KVM host for throwaway workers |
| `kuat` | UniFi USW-Flex-2.5G-8 | the switch everything docks to |

Worker VMs are satellites of their host: `byss01`, `endor02`. See [NAMING.md](NAMING.md).

### Inventory for nodes
[`inventory/nodes.yml`](inventory/nodes.yml) is the only file edited by hand. Everything in
`build/` is generated from it and committed, so a pull request shows the intent and the effect.

```sh
mise run render         # regenerate build/
mise run check          # fail if build/ is stale
mise run reservations   # for now, addressed entered by hand on Nokia app
mise run upgrade        # full-upgrade and reboot, one node at a time
```

To reach the nodes by name, add to `~/.ssh/config`:

```
Include ~/code/regal-beagle/the-place-lab/build/ssh_config
```

### Addressing

The house router is an ISP-managed Nokia with a locked LAN page and a DHCP pool spanning the
whole subnet, because dadgummit... 
The lab's addresses are carved out with per-MAC reservations entered in its mobile
app (because it grabs identity better than their web-ui). 

That step is manual; `mise run reservations` renders the list.

### Virtual machines

A VM is a roster entry like any other, plus `hypervisor`, `memory`, `vcpus` and `disk`, a
MAC of its own and an address from the VM block. Enter its reservation first; the moment its
status leaves `planned`, `mise run apply` builds it on its hypervisor — a pinned cloud image
as its disk, attached straight to the LAN through the hypervisor's NIC — and then
configures it like every other node. `mise run destroy -- <name>` takes it apart again.

### Keeping it current

Security fixes arrive nightly through unattended-upgrades and never reboot anything. The
rest is `mise run upgrade`: a full upgrade and a reboot where one is required, one node at a
time, bays first and kejim last so the dashboard watches every other node go and come back.
Run it when the Updates or Reboots tiles say so, about monthly. Container images and Python
dependencies are pinned in the files Dependabot reads, so a new release arrives as a pull
request with its notes attached, and merging plus `mise run apply` is the upgrade.
