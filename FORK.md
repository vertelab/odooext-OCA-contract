# odooext-OCA-contract — Vertel fork

## Provenance

| | |
|---|---|
| Upstream | https://github.com/OCA/contract |
| Fork | https://github.com/vertelab/odooext-OCA-contract |
| Start branch | `19.0` |
| Start commit | `b1d3126` (3 commits ahead of OCA's `882afdfb`, 0 behind) |

## Why the fork exists

OCA/contract's `20.0` branch contains no modules. Six of them block six
Vertelab modules in `odoo-contract`:

```
contract                     -> contract_edit_active_lines, contract_invoicingplan,
                                contract_monthly_value, contract_recurring_event,
                                sale_contract
contract_line_successor
contract_termination         -> contract_recurring_event
product_contract             -> sale_contract, contract_variable_qty_hour_bank
contract_variable_quantity   -> contract_variable_qty_hour_bank
contract_sale
```

Their dependencies close on the chain plus core, so no second repository is
needed. See `openspec/changes/oca-contract-nailstick/`.

## Retirement condition

When OCA publishes these modules on their `20.0` branch, this fork is retired
and any local patches are re-evaluated — not merged blindly.

## Maintenance

P-files, one source per module, expanded for 18.0, 19.0 and 20.0. The method is
`/skill:odoo-pfiles`; the coverage gate is `pfiles-check`.

## Out of scope

`contract_payment_mode` needs `account_payment_mode` from OCA/bank-payment,
whose 20.0 branch is also empty. Including it would make this a three-repo port.
