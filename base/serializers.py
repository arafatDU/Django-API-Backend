from rest_framework import serializers
from .models import Advocates, Company



class CompanySerializer(serializers.ModelSerializer):
  employee_count = serializers.SerializerMethodField(read_only=True)
  
  class Meta:
    model = Company
    fields = '__all__'
    
  def get_employee_count(self, obj):
    count = obj.advocates_set.count()
    return count



# class CompanyNameSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Company
#     fields = ['name']

class AdvocatesSerializer(serializers.ModelSerializer):
  # company = CompanyNameSerializer()
  company = serializers.CharField(source="company.name", allow_null=True, required=False)
  class Meta:
    model = Advocates
    fields = ['username', 'bio', 'company']
