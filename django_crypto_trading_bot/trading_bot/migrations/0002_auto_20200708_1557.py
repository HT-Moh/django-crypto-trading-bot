# Generated by Django 3.0.5 on 2020-07-08 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("trading_bot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bot",
            name="quote",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="trading_bot.Currency",
            ),
        ),
        migrations.AddField(
            model_name="bot",
            name="trade_mode",
            field=models.CharField(
                choices=[
                    ("wave rider", "Wave Rider"),
                    ("rising chart", "Rising Chart"),
                ],
                default="wave rider",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="bot",
            name="market",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="trading_bot.Market",
            ),
        ),
        migrations.AlterField(
            model_name="bot",
            name="timeframe",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1m", "Minute 1"),
                    ("3m", "Minute 3"),
                    ("5m", "Minute 5"),
                    ("15m", "Minute 15"),
                    ("30m", "Minute 30"),
                    ("1h", "Hour 1"),
                    ("2h", "Hour 2"),
                    ("4h", "Hour 4"),
                    ("6h", "Hour 6"),
                    ("8h", "Hour 8"),
                    ("12h", "Hour 12"),
                    ("1d", "Day 1"),
                    ("3d", "Day 3"),
                    ("1w", "Week 1"),
                    ("1M", "Month 1"),
                ],
                default="1M",
                max_length=10,
                null=True,
            ),
        ),
    ]
