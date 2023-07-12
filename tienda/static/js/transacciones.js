const query = new URLSearchParams({
    transaction_id: 'stringstringstrin',
    transaction_type: 'string',
    transaction_status: 'string',
    transaction_amount: 'string',
    transaction_currency: 'string',
    start_date: 'stringstringstringst',
    end_date: 'stringstringstringst',
    payment_instrument_type: 'string',
    store_id: 'string',
    terminal_id: 'string',
    fields: 'transaction_info',
    balance_affecting_records_only: 'Y',
    page_size: '100',
    page: '1'
}).toString();
async function test()
{
const resp = await fetch(
    `https://api-m.sandbox.paypal.com/v1/reporting/transactions?${query}`,
    {
        method: 'GET',
        headers: {
            Authorization: 'Bearer A21AAIbx2ujgaYSTOAhor_u3vUNbbROOQv6W_C3XXiylSPwIrnzoK74N2noqAYh8zJcfr991QhNN7y38-jAq40P_kFlxaNoSA'
        }
    }
);

const data = await resp.text();
console.log(data);
}