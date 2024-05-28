odoo.define('oao_select_city.form', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function () {
        console.log("TESTETETESTE111")
        $('#country').change(function () {
            var country_id = $(this).val();
            if (country_id) {
                ajax.jsonRpc('/get_states', 'call', {'country_id': parseInt(country_id)}).then(function (data) {
                    console.log(data)
                    var $state = $('#state');
                    $state.empty();
                    $state.append('<option value="">Select a state</option>');
                    $.each(data, function (index, state) {
                        $state.append($('<option>', {
                            value: state.id,
                            text: state.name
                        }));
                    });
                });
            } else {
                $('#state').empty();
                $('#state').append('<option value="">Select a state</option>');
            }
        });
    });
});
