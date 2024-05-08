odoo.define('pos_reciept.models', function (require) {
    "use strict";

    var { Order } = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');
    const CustomOrder = (Order) => class CustomOrder extends Order {
        export_for_printing() {
            var result = super.export_for_printing(...arguments);
            result.total_amount = this.get_total_with_tax();
            result.qr = this._get_qr_code_data();
            result.order_number = this._get_order_number();
            result.client = this._get_employee_name();
            result.custom_footer = this._get_footer_from_shop();
            // as on order lines get the product name and check if it have barcode for example [1234] abc than remove it for example abc otherwise return it
            result.orderlines = result.orderlines.map((line) => {
                if (line.product_name_wrapped[0].indexOf("[") > -1 && line.product_name_wrapped[0].indexOf("]") > -1) {
                    line.product_name_wrapped[0] = line.product_name_wrapped[0].substring(line.product_name_wrapped[0].indexOf("]") + 1);
                }
                return line;
            });
            return result;
        }
        



        _get_employee_name(){
            if(this.pos.get_cashier()){
                return this.pos.get_cashier().name;

            }
            return "";
        }
        _get_order_number(){
            if(this.pos.config.pos_order_number){
                return this.pos.config.pos_order_number_prefix + this.uid;
            }
            return this.uid;
        }
        _get_qr_code_data() {
            if (this.pos.company.point_of_sale_use_ticket_qr_code) {
                // Construct the URL with the desired parameters and order data
                const configId = 2; // Replace this with the desired config_id
                const orderData = { cids: [1] }; // Replace [1] with the desired order IDs
                const queryString = new URLSearchParams(orderData).toString();
                const url = this._get_order_number();
                
        
                // Generate the QR code for the constructed URL
                const codeWriter = new window.ZXing.BrowserQRCodeSvgWriter();
                const qr_code_svg = new XMLSerializer().serializeToString(codeWriter.write(url, 150, 150));
                return "data:image/svg+xml;base64," + window.btoa(qr_code_svg);
            } else {
                return false;
            }
        }


        _get_footer_from_shop(){
            if(this.pos.config.custom_footer){
                console.log(this.pos.config.custom_footer);

                return this.pos.config.custom_footer;
            }
            console.log("Not Found");

            return "";
            
        }
        
    }
    
    Registries.Model.extend(Order, CustomOrder);
});


