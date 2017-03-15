import EmberUploader from 'ember-uploader';

export default EmberUploader.FileField.extend({

    filesDidChange: function(files) {

        Ember.$.ajax({
            type: 'GET',
            url: 'http://localhost:8000/get_signed_url',
            crossDomain: true,
            success: function(url) {
                const uploader = EmberUploader.Uploader.create({
                    url: url
                });
                if (!Ember.isEmpty(files)) {
                    uploader.upload(files[0], {});
                }
            },
            error: function(request, textStatus, errorThrown) {
                alert(errorThrown);
                console.log();
            }
        });

    }

});
