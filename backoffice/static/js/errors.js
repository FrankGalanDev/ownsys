function launcherrormodal{

	{%if messages%}
		var html = '<p>';
		    {% for message in messages %}
	            html += '{{message }} <br>';
	        {% endfor %}

	    html = '</p>';
	    #errorModal;

}