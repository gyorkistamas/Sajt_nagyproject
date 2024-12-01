from email import message
from django.core.cache import cache
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from flask import redirect
from .models import Translation

def add_translation(request):
    if request.method == "POST":
        lang_code = request.POST.get("lang_code")
        key = request.POST.get("key")
        text = request.POST.get("text")
        translation, created = Translation.objects.update_or_create(
            key=key, lang_code=lang_code,
            defaults={"text": text}
        )
        return JsonResponse({"success": True, 'created': created})
    return JsonResponse({"success": False, 'error': False})


def translation_list(request):
    translations = Translation.objects.all()
    return render(request, 'localization_framework/translation_list.html', {'translations': translations})

def add_translation(request):
    if request.method == "POST":
        lang_code = request.POST.get("lang_code")
        key = request.POST.get("key")
        text = request.POST.get("text")
        
        if Translation.objects.filter(key=key, lang_code=lang_code).exists():
            return JsonResponse({"success": False, 'error': 'Translation with this key already exists'})
        else:            
            Translation.objects.create(key=key, lang_code=lang_code, text=text)
            message.success(request, "Translation added successfully")
            return redirect('translation_list')

    return render(request, 'localization_framework/add_translation.html')


def edit_translation(request, pk):
    translation = get_object_or_404(Translation, pk=pk)

    if request.method == "POST":
        lang_code = request.POST.get("lang_code")
        key = request.POST.get("key")
        text = request.POST.get("text")

        translation.lang_code = lang_code
        translation.key = key
        translation.text = text
        translation.save()
        cache.delete(f"translation_{translation.lang_code}_{translation.key}")
        messages.success(request, "Translation updated successfully")
        return redirect('translation_list')

    return render(request, 'localization_framework/edit_translation.html', {'translation': translation})

def delete_translation(request, pk):
    translation = get_object_or_404(Translation, pk=pk)
    cache.delete(f"translation_{translation.lang_code}_{translation.key}")
    translation.delete()
    messages.success(request, "Translation deleted successfully")
    return redirect('translation_list')

def mass_add_translation(request):
    if request.method == "POST":
        translation_data = request.POST.get('translation_data', '')
        added, skipped = 0, 0
        for line in translation_data.strip().split('\n'):
            try:
                key, language_code, text = line.split('|', 2)
                if Translation.objects.filter(key=key, lang_code=language_code).exists():
                    skipped += 1
                else:
                    Translation.objects.create(key=key, lang_code=language_code, text=text)
                    added += 1
            except ValueError:
                skipped += 1
        messages.success(request, f"Added: {added} Skipped: {skipped}")
        return redirect('translation_list')
    
    return render(request, 'localization_framework/mass_add_translation.html')

def mass_edit_translation(request):
    if request.method == "POST":
        translation_data = request.POST.get('translation_data', '')
        updated, skipped = 0, 0
        for line in translation_data.strip().split('\n'):
            try:
                key, language_code, text = line.split('|', 2)
                translation = Translation.objects.filter(key=key, lang_code=language_code).first()
                if translation:
                    translation.text = text
                    translation.save()
                    updated += 1
                else:
                    skipped += 1
            except ValueError:
                skipped += 1
                
        messages.success(request, f"Updated: {updated} Skipped: {skipped}")
        return redirect('translation_list')
    
    return render(request, 'localization_framework/mass_edit_translation.html')

def mass_delete_translation(request):
    if request.method == "POST":
        keys = request.POST.get('keys', '').strip().split('\n')
        deleted, skipped = 0, 0
        
        for key in keys:
            translations = Translation.objects.filter(key=key)
            if translations.exists():
                for translation in translations:
                    cache.delete(f"translation_{translation.lang_code}_{translation.key}")
                translations.delete()
                deleted += translations.count()
            else:
                skipped += 1
                
        messages.success(request, f"Deleted: {deleted} Skipped: {skipped}")
        return redirect('translation_list')
    
    return render(request, 'localization_framework/mass_delete_translation.html')