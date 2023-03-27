Java.perform(function() {
    var hook = Java.use('com.gamevil.nexus2.xml.NexusTorchwood');
    hook.onPostExecute.overload('java.lang.String').implementation = function(){
        // remove popup
    }
});

rpc.exports = {
    get : function(type, value){
        Java.perform(function() {
            var hook = Java.use('com.gamevil.cartoonwars.two.JNINatives');
            hook.nativeOnTstorePreDeposit(type, value);
        });
    }
};
